from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

# Load the processor and model from transformers library
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load an image from a URL
image_url = "https://images.unsplash.com/photo-1550340497-21e9bd6dc9b8"  # Sample image URL
image = Image.open(requests.get(image_url, stream=True).raw)

# Prepare the image and generate caption
inputs = processor(images=image, return_tensors="pt")
outputs = model.generate(**inputs)

# Decode the generated caption
caption = processor.decode(outputs[0], skip_special_tokens=True)

print("Generated Caption:", caption)
r
