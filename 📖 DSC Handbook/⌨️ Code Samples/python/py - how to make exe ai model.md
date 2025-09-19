---
type: Code Snippet
---

- In python you can use the `pyinstaller` package to create an exe of any python app
- I have found a way to turn a machine learning model into a model of use. Example i created this small app that takes a premise and hypothesis to show the entailment. This exe file can be ran on any computer so long as it was compiled on the same architecture. For example for me to use it on linux i would need to create the app in linux then build it on there. Here is the example code.
-
- (1) Download your model of choice
- (2) Setup your python file to do what you need
- ```
  import tkinter as tk
  from tkinter import messagebox
  from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
  import os
  
  class NLIApp:
      def __init__(self, root):
          self.root = root
          self.root.title("Entailment Classifier")
          self.root.geometry("500x300")
  
          tk.Label(root, text="Premise:").pack(pady=(10, 0))
          self.premise_entry = tk.Entry(root, width=60)
          self.premise_entry.pack()
  
          tk.Label(root, text="Hypothesis:").pack(pady=(10, 0))
          self.hypothesis_entry = tk.Entry(root, width=60)
          self.hypothesis_entry.pack()
  
          self.button = tk.Button(root, text="Check Entailment", command=self.evaluate)
          self.button.pack(pady=15)
  
          self.result_label = tk.Label(root, text="", font=("Arial", 12))
          self.result_label.pack(pady=10)
  
          self.load_model()
          # Disclaimer at the bottom
          disclaimer = "2025 | Using MNLI-trained transformer model | For testing only | Issues consult phillip.hungerford"
          self.footer = tk.Label(root, text=disclaimer, font=("Arial", 8), fg="gray")
          self.footer.pack(side="bottom", pady=(10, 5))
  
  
      def load_model(self):
          model_dir = os.path.join(os.path.dirname(__file__), "model")
          self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
          self.model = AutoModelForSequenceClassification.from_pretrained(model_dir)
          self.classifier = pipeline("zero-shot-classification", model=self.model, tokenizer=self.tokenizer)
  
      def evaluate(self):
          premise = self.premise_entry.get()
          hypothesis = self.hypothesis_entry.get()
  
          if not premise or not hypothesis:
              messagebox.showwarning("Missing Input", "Please fill in both premise and hypothesis.")
              return
  
          try:
              result = self.classifier(premise, [hypothesis])
              score = round(result['scores'][0], 3)
              self.result_label.config(text=f"Entailment Score: {score}")
          except Exception as e:
              messagebox.showerror("Model Error", f"An error occurred:\n{e}")
  
  if __name__ == "__main__":
      root = tk.Tk()
      app = NLIApp(root)
      root.mainloop()
  
  ```
- ![image.png](../assets/image_1751346410914_0.png)
	- Run pyinstaller to turn it into an executable and thats it!
	- ```
	  #install if you need to
	  !pip install pyinstaller --trusted-host pypi.org --trusted-host files.pythonhosted.org
	  
	  pyinstaller --onefile --add-data "model:model" --collect-submodules transformers nli_cli.py
	  ```
	- If you have issues with packages or dependencies make sure to include the collect-submodules
	- file will be stored in the dist folder
		- `dist/package.exe`