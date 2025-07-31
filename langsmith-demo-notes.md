TECHNICAL DETAILS
    1. Tracing
        a. Brief overview of LangSmith portal/UI
        b. Based on open-source OpenTelemetry standard
        c. How to send telemetry data to LangSmith? Account + API keys + environment variables + @traceable
        d. Can be used without LangChain + LangGraph!
        e. EXAMPLE 1 then show UI (tracing, runs, inputs/outputs, cost, latency, run types, waterfall)
        f. If using LangGraph, the traceability comes out of the box, don't even need to tag your functions with decorator
    2. Playground & Prompts
        a. Features for optimizing, iterating, and collaborating on your LLM prompts.
        b. Grab prompt from tracing, then change it once. Show how you can change models and parameters.
        c. Save to prompt hub (with input variables). Show commits/versioning.
        d. Use prompt code from hub in your app and run again.
        e. Show Prompt Canvas (if there is time) and rerun app
    3. Datasets & Evaluations
        a. Dataset: collection of data you want to test your application against. Can be FAQ, edge cases, etc.
            i. Define input/output schema
            ii. Explain golden dataset: common pattern in industry where you collect ideal responses to evaluate your app against
            iii. Manually create examples in dataset
            iv. Can also add AI generated examples
            v. Can also add from previous traces (in bulk too)
        b. Experiments
            i. Will run latest version of your application against every example in your dataset. And then compare resulting outputs to our reference outputs from dataset
            ii. SDK EXAMPLE (with a different model perhaps from a previous run?)
                1) Define Evaluators
                    a) Custom Code evaluator
                    b) Or LLM-as-Judge evaluator
                2) Run and go over results in UI
                3) Show pre-built evaluators
                4) Compare multiple experiments
    4. Annotation Queues
        a. Way for developers and SMEs to provide feedback on your application use. Collaboration!
        b. Create annotation queue
            i. What desired feedback do you want? # of reviewers on a run? Reservation on runs?
            ii. Add existing traces to the queue
            iii. Go through queue and provide feedback. Add to golden dataset if correct?
    5. Automations & Online Evaluations
        a. Run on live, production user interactions
        b. Add automation via Rules in tracing project
            i. Show filters, sampling rate, actions
            ii. Explain chaining (Judge to add feedback that then adds trace to annotation queue)
            iii. Check logs of rules to see actions taken
            iv. Also directly check traces to see auto evaluator feedback
    6. Dashboards
        a. Prebuilt Dashboards: out of the box
        b. Create a custom dashboard
            i. Can choose multiple projects
Filter on certain traces. Choose metrics to display.