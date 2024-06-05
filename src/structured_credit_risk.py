from enum import Enum
from pathlib import Path

from distilabel.llms import LlamaCppLLM
from distilabel.pipeline import Pipeline
from distilabel.steps import LoadDataFromDicts
from distilabel.steps.tasks import TextGeneration
from pydantic import BaseModel, conint
from typing_extensions import Annotated

class EmploymentStatus(str, Enum):
    employed = "employed"
    self_employed = "self_employed"
    unemployed = "unemployed"
    student = "student"
    retired = "retired"

class CreditApplication(BaseModel):
    debt_to_income_ratio: conint(ge=0, le=100)
    employment_status: EmploymentStatus
    utilization_rate_of_revolving_credit: conint(ge=0, le=100)
    length_of_oldest_trade: conint(ge=0, lt=1000)
    number_of_delinquent_trades_in_last_24_months: conint(ge=0, lt=100)
    credit_inquiries: conint(ge=0, lt=100)
    application_approved: bool
    performance: bool

model_path = "models/openhermes-2.5-mistral-7b.Q4_K_M.gguf"

with Pipeline("Credit-Card-Applications") as pipeline:
    system_prompt = (
        "You are a credit analyst. You have reviewed thousands of credit card applications."
        " Please return a JSON object with common attributes of a credit card application."
    )

    load_dataset = LoadDataFromDicts(
        name="load_instructions",
        data=[
            {
                "system_prompt": system_prompt,
                "instruction": "Generate a credit card application with the following attributes:",
            }
        ],
    )
    llm = LlamaCppLLM(
        model_path=str(model_path),  # type: ignore
        n_gpu_layers=-1,
        n_ctx=1024,
        structured_output={"format": "json", "schema": CreditApplication},
    )
    text_generation = TextGeneration(
        name="text_generation_credit_card",
        llm=llm,
        input_batch_size=8,
        output_mappings={"model_name": "generation_model"},
    )
    load_dataset >> text_generation


if __name__ == "__main__":
    distiset = pipeline.run(
        parameters={
            text_generation.name: {
                "llm": {"generation_kwargs": {"max_new_tokens": 256}}
            }
        },
        use_cache=False,
    )
    for num, application in enumerate(distiset["default"]["train"]["generation"]):
        print(f"Application: {num}")
        print(application)

# Application: 0
# {
# "debt_to_income_ratio": 30,
# "employment_status": "employed",
# "utilization_rate_of_revolving_credit": 60,
# "length_of_oldest_trade": 60,
# "number_of_delinquent_trades_in_last_24_months": 0,
# "credit_inquiries": 2,
# "application_approved": true,
# "performance": false
# }
# ...