from transformers import BlipProcessor, BlipForConditionalGeneration, BlipForQuestionAnswering
from PIL import Image
import torch

processor_cap = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model_cap = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

processor_vqa = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model_vqa = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

def generate_caption(image_path):
    try:
        raw_image = Image.open(image_path).convert('RGB')
        inputs = processor_cap(raw_image, return_tensors="pt")
        
        
        out = model_cap.generate(
            **inputs, 
            max_new_tokens=50,
            min_length=20,
            num_beams=3,
            repetition_penalty=1.5
        )
        return processor_cap.decode(out[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error processing image: {str(e)}"

def answer_question(image_path, question):
    try:
        raw_image = Image.open(image_path).convert('RGB')
        
        inputs = processor_vqa(raw_image, question, return_tensors="pt")
        out = model_vqa.generate(**inputs)
        
        return processor_vqa.decode(out[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error answering question: {str(e)}"

if __name__ == "__main__":
    print("Both models loaded successfully. Ready for inference.")