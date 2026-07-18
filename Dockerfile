# Python 3.9 ကို အခြေခံထားတဲ့ ပေါ့ပါးတဲ့ Image ကို သုံးပါတယ်
FROM python:3.9-slim

# Bot အတွက် Folder တစ်ခု ဆောက်ပေးပါတယ်
WORKDIR /app

# လက်ရှိ ဖိုင်အားလုံးကို Container ထဲ ကူးထည့်ပါတယ်
COPY . .

# လိုအပ်တဲ့ Library တွေကို Install လုပ်ပါတယ်
RUN pip install --no-cache-dir -r requirements.txt

# Bot ကို စတင်လည်ပတ်စေပါတယ်
CMD ["python", "main.py"]
