tags:: #code/python

- setup
	- save model somewhere:
		- model e.g. [facebook_bart_mnli](https://huggingface.co/facebook/bart-large-mnli/tree/main)
			- config.json
			- pytorch_model.bin
			- tokenizer.json
			- vocab.json
- ```
  import sys
  import json
  import os
  import re
  
  def extract_sentence_with_keyword(text, keyword="metastasis", max_words=200):
      
      sentences = re.split(r'(?<=[.!?])\s+', text)
      
      for sentence in sentences:
          if re.search(r'\b' + re.escape(keyword) + r'\b', sentence, re.IGNORECASE):
              words = sentence.split()
              if len(words) <= max_words:
                  return sentence.strip()
              else:
                  
                  keyword_pos = next(
                      (i for i, word in enumerate(words) if keyword.lower() in word.lower()), -1
                  )
                  
                  start = max(0, keyword_pos - max_words // 2)
                  end = min(len(words), start + max_words)
                  truncated_words = words[start:end]
                  
  
  # ========== THREAD LIMITING ==========
  # os.environ["OMP_NUM_THREADS"] = "1"
  # os.environ["OPENBLAS_NUM_THREADS"] = "1"
  # os.environ["MKL_NUM_THREADS"] = "1"
  # os.environ["NUMEXPR_NUM_THREADS"] = "1"
  
  # ========== INPUT CHECK ==========
  if len(sys.argv) < 2:
      print(json.dumps({"error": "No input text provided"}))
      sys.exit(1)
  
  input_text = sys.argv[1].strip()
  if not input_text:
      print(json.dumps({"error": "Empty input text"}))
      sys.exit(1)
  
  text = extract_sentence_with_keyword(input_text, keyword="metastasis", max_words=200)
  
  # ========== MODEL INFERENCE ==========
  try:
      from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
  
      model_dir = '../../Models/facebook_bart_mnli'
  
      # Ensure model exists locally
      if not os.path.exists(model_dir):
          raise FileNotFoundError(f"Model directory not found: {model_dir}")
  
      # Load tokenizer and model from local directory only
      tokenizer = AutoTokenizer.from_pretrained(model_dir, local_files_only=True)
      model = AutoModelForSequenceClassification.from_pretrained(model_dir, local_files_only=True)
  
      # Set up zero-shot classification pipeline
      classifier = pipeline(
          'zero-shot-classification',
          model=model,
          tokenizer=tokenizer
      )
  
      # Define labels
      metastasis_labels = ['metastasis present', 'no metastasis present']
  
      # Run classification
      result = classifier(text, metastasis_labels)
      scores = {label: score for label, score in zip(result['labels'], result['scores'])}
      score = scores.get('metastasis present', 0.0)
  
      # Return score as JSON
      print(score)
  
      # print(json.dumps({"score": score}))
  
  except Exception as e:
      # Return error as JSON if anything fails
      print(json.dumps({"error": str(e)}))
      sys.exit(1)
  
  ```