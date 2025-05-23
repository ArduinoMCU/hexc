# 🔧 hexc — HEX to C Header Converter

`hexc` হলো একটি ছোট ও কার্যকরী কমান্ড লাইন টুল, যা Intel HEX ফাইলকে C ভাষার header ফাইলে রূপান্তরিত করে। এটি বিশেষভাবে তৈরি করা হয়েছে embedded systems প্রকল্পের জন্য যেমন Arduino প্রোগ্রামিং, যেখানে `.hex` ফাইলের কন্টেন্ট সরাসরি C কোডে ব্যবহারের প্রয়োজন হয়।

---

## 🧩 বৈশিষ্ট্য

- Intel HEX ফাইল থেকে সরাসরি `PROGMEM` C array তৈরি করে।
- `#define` guard নাম কাস্টমাইজ করা যায়।
- কমান্ড-লাইন ইন্টারফেস (CLI) সরল ও ব্যবহার-বান্ধব।
- অতিরিক্ত তথ্য দেখানোর জন্য `--verbose` অপশন।
- কম্প্রেসড ও অপ্টিমাইজড `.exe`।

---

## 🔍 ব্যবহারিক প্রয়োগ

Arduino বা অন্য AVR ভিত্তিক মাইক্রোকন্ট্রোলারে যখন বুটলোডার বা firmware C প্রোগ্রামের মধ্যে embed করতে হয়, তখন এই টুলটি ব্যবহৃত হয়।

### উদাহরণ:

```bash
hexc.exe firmware.hex --define-name=headerfilename
