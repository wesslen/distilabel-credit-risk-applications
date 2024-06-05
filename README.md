# Intro

Local (`llama-cpp`) with HF quantized Mistral7B generates structured (`pydantic`) synthetic credit card application data with `distilabel`.

# Setup

```
python3.11 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
make install-llama-cpp
make download-llm
```

Then run:

```
$ python src/structured_credit_risk.py
[06/05/24 11:38:00] INFO     ['distilabel.pipeline.local'] 📝 Pipeline data will be written to                                                        local.py:128
                             '/Users/ryan/.cache/distilabel/pipelines/Credit-Card-Applications/38d9de0f1f8de0e06ce94dabe53ca3de12bb51fc/data'                     
[06/05/24 11:38:02] INFO     ['distilabel.pipeline.local'] ⏳ Waiting for all the steps to load...                                                    local.py:469
[06/05/24 11:38:04] INFO     ['distilabel.pipeline.local'] ⏳ Steps loaded: 1/2                                                                       local.py:483
Compiling FSM index for all state transitions: 100%|████████████████████████████████████████████████████████████████████████████| 307/307 [00:06<00:00, 44.14it/s]
[06/05/24 11:38:17] INFO     ['distilabel.pipeline.local'] ⏳ Steps loaded: 2/2                                                                       local.py:483
                    INFO     ['distilabel.pipeline.local'] ✅ All the steps have been loaded!                                                         local.py:487
                    INFO     ['distilabel.step.load_instructions'] 🧬 Starting yielding batches from generator step 'load_instructions'. Offset: 0    local.py:911
                    INFO     ['distilabel.step.load_instructions'] 📨 Step 'load_instructions' sending batch 0 to output queue                        local.py:998
                    INFO     ['distilabel.step.load_instructions'] 🏁 Finished running step 'load_instructions'                                       local.py:880
                    INFO     ['distilabel.step.text_generation_credit_card'] 📦 Processing batch 0 in 'text_generation_credit_card'                   local.py:960
[06/05/24 11:38:41] INFO     ['distilabel.step.text_generation_credit_card'] 📨 Step 'text_generation_credit_card' sending batch 0 to output queue    local.py:998
                    INFO     ['distilabel.step.text_generation_credit_card'] 🏁 Finished running step 'text_generation_credit_card'                   local.py:880
Generating train split: 1 examples [00:00, 556.42 examples/s]
Application: 0
{"debt_to_income_ratio": 35, "employment_status": "employed", "utilization_rate_of_revolving_credit": 20, "length_of_oldest_trade": 4, "number_of_delinquent_trades_in_last_24_months": 1, "credit_inquiries": 3, "application_approved": false, "performance": false}
```