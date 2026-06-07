
# Multimodal Vision-Language AI: Image Understanding & VQA

## 📌 Overview
This project is an intelligent computer vision web application developed to perform advanced image understanding. Moving beyond traditional image processing, this system utilizes deep learning and modern **Vision-Language Models (VLMs)** to fuse visual and textual modalities. 

The application provides an interactive, user-friendly interface where users can upload images to automatically generate highly detailed contextual descriptions, and utilize **Visual Question Answering (VQA)** to ask specific natural language questions about the visual data.

## 🚀 Key Features

* **Advanced Image Captioning:** Utilizes a pre-trained BLIP (Bootstrapping Language-Image Pre-training) foundation model to generate descriptive text based on visual inputs.
* **Visual Question Answering (VQA):** Features a secondary multimodal AI engine that processes both an image and a user-defined text query simultaneously to provide precise, context-aware answers.
* **Optimized Text Generation:** The underlying model parameters are heavily optimized using Beam Search (`num_beams=3`), length constraints (`min_length=20`, `max_new_tokens=50`), and repetition penalties (`1.5`) to ensure rich, non-repetitive vocabulary.
* **Interactive Web Interface:** A lightweight, responsive web interface built with Flask, HTML, and CSS that handles file uploads, securely processes data, and dynamically renders the AI's visual analysis.
* **Local Inference:** Runs deep neural network tensor operations locally using PyTorch without relying on external paid APIs.

## 🛠️ Technology Stack

* **Backend Framework:** Python, Flask, Werkzeug
* **Deep Learning Engine:** PyTorch (`torch`), Torchvision
* **AI Models:** Hugging Face `transformers` 
  * Captioning: `Salesforce/blip-image-captioning-base`
  * VQA: `Salesforce/blip-vqa-base`
* **Image Processing:** Python Imaging Library (`PIL`)
* **Frontend:** HTML5, CSS3, Jinja2 Templating

## ⚙️ Installation & Setup

To run this application locally, ensure you have Python 3.8+ installed on your system. 

**1. Clone the repository**
```bash
git clone [https://github.com/AgrimGangwar25/Image-captioning-using-VLM.git](https://github.com/AgrimGangwar25/Image-captioning-using-VLM.git)
cd Image-captioning-using-VLM