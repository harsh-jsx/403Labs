# How to Demonstrate Caller ID Spoofing to Students

## 🎯 The Educational Goal

Show students:
1. **How caller ID spoofing works** (technically)
2. **Why legitimate services prevent it** (security)
3. **How malicious services allow it** (the problem)

## 📋 What You'll Demonstrate

### Demo 1: Legitimate Call (Works ✅)
- Call from your verified Twilio number
- Shows normal, legitimate calling
- Call succeeds

### Demo 2: Spoofing Attempt (Fails ✅ - This is the point!)
- Attempt to call from an unverified number
- Twilio REJECTS it (security feature)
- Explains why this is good
- Shows how malicious services differ

## 🚀 How to Run the Demo

### Step 1: Set Up
1. Make sure you have `config.json` with your Twilio credentials
2. Install dependencies: `pip install -r requirements.txt`

### Step 2: Customize the Spoofed Number
Edit `phone_demo.py` around line 415:

```python
# Change this to any number you want to demonstrate with
spoofed_number = "+15551234567"  # Change to any unverified number
```

**Good examples for demo:**
- `+15551234567` (fake US number)
- `+12125551234` (fake US number)
- `+447911123456` (fake UK number)
- Any number you don't own/verify

### Step 3: Run the Demo
```bash
python phone_demo.py
```

## 📚 What Students Will See

### Demo 1: Legitimate Call
- ✅ Call succeeds (if recipient is verified)
- Shows normal calling behavior
- Uses verified Twilio number

### Demo 2: Spoofing Attempt
- ❌ Call FAILS (this is the educational point!)
- Error message explains why
- Shows security feature in action

## 🎓 Teaching Points

### When Demo 2 Fails, Explain:

1. **Why It Failed:**
   - Twilio verified the caller ID
   - Number wasn't verified → call rejected
   - This is a SECURITY FEATURE

2. **How Scammers Do It:**
   - Use unverified VoIP providers
   - Those providers don't verify caller IDs
   - They can set ANY number
   - Phone networks trust and display it

3. **The Key Difference:**
   - **Legitimate services (Twilio):** Verify → Prevent spoofing ✅
   - **Malicious services:** Don't verify → Allow spoofing ❌

4. **Why Phone Networks Trust It:**
   - Legacy systems trust caller ID from SIP header
   - No universal verification system
   - Unverified services don't check ownership

## 💡 Classroom Discussion Questions

1. **Why do you think Twilio rejects unverified numbers?**
   - Security, compliance, user protection

2. **How do scammers get around this?**
   - Use unverified providers that don't check

3. **What could be done to prevent spoofing?**
   - STIR/SHAKEN protocol
   - Better verification systems
   - Education and awareness

4. **Is caller ID spoofing always bad?**
   - No - legal for legitimate business
   - Yes - when used for fraud/harassment

## ⚠️ Important Notes

- **The failure is the point!** It shows security working
- **Don't try to actually spoof** - this is educational
- **Emphasize legal/ethical use** throughout
- **Explain the difference** between legitimate and malicious services

## 🔧 Troubleshooting

### If Demo 1 Fails:
- Recipient number might not be verified (trial account limitation)
- Verify the number in Twilio console first
- Or upgrade to paid account

### If Demo 2 Succeeds (unlikely):
- Check if the number is actually verified
- Use a clearly fake number (like +15551234567)
- This shouldn't happen with Twilio

## 📖 Additional Resources

- See `HOW_IT_WORKS.md` for technical details
- See `CLASS_DEMO_GUIDE.md` for full class structure
- See `README.md` for setup instructions

