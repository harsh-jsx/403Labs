# Class Demo Guide: Understanding Caller ID Spoofing

## 🎯 Learning Objectives

By the end of this demo, students should understand:

1. How VoIP (Voice over IP) calls work
2. How caller ID information is transmitted
3. Why caller ID spoofing is technically possible
4. The difference between legitimate and malicious services
5. Security implications and countermeasures

## 📋 Pre-Demo Setup (Before Class)

1. **Set up Twilio account** (if you haven't already):

   - Go to https://www.twilio.com/try-twilio
   - Sign up for free trial
   - Get Account SID and Auth Token from dashboard
   - Purchase a phone number (or use trial number)

2. **Install and configure the demo:**

   ```bash
   pip install -r requirements.txt
   cp config.example.json config.json
   # Edit config.json with your Twilio credentials
   ```

3. **Test the demo** (optional - you can show it live):
   - Run: `python phone_demo.py`
   - Verify it connects to Twilio

## 🎬 Demo Flow (30-45 minutes)

### Part 1: Introduction (5 minutes)

**Opening Question:**
"Has anyone ever received a call that appeared to be from a local number, but when you answered, it was a scammer or telemarketer? How do you think they do that?"

**Key Points:**

- Explain that this is caller ID spoofing
- It's a real problem affecting millions of people
- Today we'll understand the technology behind it

### Part 2: How Phone Calls Work (10 minutes)

**Explain the basics:**

1. **Traditional Landlines:**

   - Caller ID was sent by the phone company
   - Harder to spoof (but not impossible)
   - Trusted system

2. **VoIP (Voice over IP):**
   - Calls travel over the internet
   - Use SIP (Session Initiation Protocol)
   - Caller ID is in the SIP header
   - Can be manipulated more easily

**Show the code:**

```python
call = self.client.calls.create(
    to=to_number,
    from_=from_number,  # This sets the caller ID!
    url="http://your-server.com/call-handler"
)
```

**Key Insight:** The `from_` parameter is what appears as caller ID. The phone network trusts this information.

### Part 3: Legitimate vs. Malicious Services (10 minutes)

**Show the difference:**

1. **Legitimate Services (Twilio):**

   - ✅ Verify phone numbers before use
   - ✅ Only allow numbers you own/verify
   - ✅ Provide audit trails
   - ✅ Comply with regulations
   - ✅ Used for legitimate business

2. **Malicious Services:**
   - ❌ Don't verify caller IDs
   - ❌ Allow any number to be used
   - ❌ No accountability
   - ❌ Often operate from lax jurisdictions
   - ❌ Used for scams and harassment

**Demo Point:** Show that with Twilio, you can only use verified numbers. Try to use an unverified number - it will fail.

### Part 4: Why It Works (5 minutes)

**Explain the technical reasons:**

1. **Trust-based system:**

   - Phone networks trust the caller ID from SIP header
   - No universal verification system exists
   - Legacy systems weren't designed for security

2. **The Problem:**

   - Scammers use unverified VoIP providers
   - They can set any caller ID
   - Phone networks display it as-is
   - Recipients trust what they see

3. **The Solution (STIR/SHAKEN):**
   - New protocol for caller ID verification
   - Being rolled out in the US and other countries
   - Helps identify verified vs. spoofed calls

### Part 5: Legal and Ethical Discussion (10 minutes)

**Key Questions for Discussion:**

1. **When is caller ID spoofing legal?**

   - Legitimate business (with proper disclosure)
   - Law enforcement (with proper authorization)
   - Privacy protection (e.g., doctors calling patients)

2. **When is it illegal?**

   - Fraud or scams
   - Harassment or stalking
   - Impersonation
   - Violating telemarketing regulations

3. **What are the consequences?**

   - Criminal charges
   - Civil lawsuits
   - FCC fines (up to $10,000 per violation in US)

4. **How can we protect ourselves?**
   - Don't trust caller ID alone
   - Be skeptical of unknown callers
   - Never give personal info over the phone
   - Use call blocking apps
   - Report suspicious calls

### Part 6: Live Demo (Optional - 5 minutes)

**If you want to show a live call:**

1. **Set up webhook server** (use ngrok for local):

   ```bash
   ngrok http 5000
   ```

2. **Update callback URL** in code

3. **Make a test call** to your own phone:

   ```python
   demo.make_call(
       to_number="+1YOUR_PHONE_NUMBER",
       message="This is an educational demo call."
   )
   ```

4. **Show students** that the caller ID appears as your Twilio number

## 💡 Discussion Questions

1. **Technical:**

   - Why do phone networks trust caller ID information?
   - What could be done to prevent spoofing?
   - How does STIR/SHAKEN work?

2. **Ethical:**

   - Is caller ID spoofing ever justified?
   - What's the difference between legitimate and malicious use?
   - How should we balance privacy and security?

3. **Legal:**

   - Should caller ID spoofing be completely banned?
   - What are the challenges in enforcing anti-spoofing laws?
   - How do different countries handle this?

4. **Practical:**
   - How can individuals protect themselves?
   - What should companies do to prevent spoofing?
   - How can technology help solve this problem?

## 📊 Assessment Ideas

1. **Short Essay:**

   - "Explain how caller ID spoofing works and why it's possible. Discuss the difference between legitimate and malicious use."

2. **Code Review:**

   - Have students identify the key line that sets caller ID
   - Ask them to explain why this works

3. **Case Study:**

   - Present a real-world spoofing case
   - Have students analyze the technical and legal aspects

4. **Design Challenge:**
   - "Design a system to prevent caller ID spoofing. What technical and policy measures would you implement?"

## ⚠️ Important Reminders

- **Emphasize legal/ethical use only**
- **This is for educational understanding, not exploitation**
- **Always check local laws before using any calling technology**
- **Respect privacy and consent**

## 📚 Additional Resources for Students

- [FCC Caller ID Spoofing Information](https://www.fcc.gov/spoofing)
- [STIR/SHAKEN Protocol](https://www.fcc.gov/call-authentication)
- [Twilio Documentation](https://www.twilio.com/docs)
- [SIP Protocol RFC](https://tools.ietf.org/html/rfc3261)

## 🎯 Key Takeaways

1. Caller ID spoofing works because phone networks trust caller ID information
2. VoIP makes spoofing easier than traditional phone systems
3. Legitimate services verify numbers; malicious services don't
4. It's illegal for fraud/harassment but legal for legitimate business
5. New protocols like STIR/SHAKEN are being developed to prevent spoofing
6. Technology alone won't solve this - education and awareness are crucial
