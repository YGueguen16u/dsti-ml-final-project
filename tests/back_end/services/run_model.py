from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_id = "teknium/OpenHermes-2.5-Mistral-7B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="cpu")  # Compatible Mac

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

while True:
    user_input = input("👤> ")
    prompt = f"""Tu es un assistant de santé qui retourne un JSON avec assistant_output et commands.
Texte utilisateur : "{user_input}" """
    out = pipe(prompt, max_new_tokens=512, temperature=0.7, do_sample=True)
    print(out[0]["generated_text"])