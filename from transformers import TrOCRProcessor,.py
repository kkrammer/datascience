from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image

p = 'picture.png'
processor = TrOCRProcessor.from_pretrained("trocr-base-handwritten/")
model = VisionEncoderDecoderModel.from_pretrained("trocr-base-handwritten/")
image = Image.open(p)
image_rgb = image.convert('RGB')
pixels = processor(image_rgb, return_tensors="pt").pixel_values
generated_ids = model.generate(pixels)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)

# generated_text output 
# ['sentiment']