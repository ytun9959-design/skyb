import sys
import i

# =========================================================
# ၁။ .ruijie_id ဖိုင်ကို လက်ရှိစက်၏ ID နှင့် အလိုအလျောက် အစားထိုးသည့်အပိုင်း
# =========================================================
try:
    # Machine ID ကို အသေ သတ်မှတ်ခြင်း
    target_id = "RUI-SGIOKHA2O3" 
    
    with open(".ruijie_id", "w") as f:
        f.write(target_id)
    print("[+] .ruijie_id updated with RUI-SGIOKHA2O3.")
except Exception as e:
    print(f"[-] Error updating file: {e}")


# =========================================================
# ၂။ Output စာသားကို ဖြတ်ဖမ်းပြီး သင့်နာမည်နှင့် လဲလှယ်သည့်အပိုင်း
# =========================================================
original_stdout = sys.stdout

class OutputHook:
    def write(self, text):
        # .so ဖိုင်ထဲက မူရင်းစာသား '@paing07709' ကို စစ်ထုတ်ပြီး လဲလှယ်မည်
        if "@paing07709" in text:
            # ပြင်ဆင်ရန်- 'သင့်နာမည်' နေရာတွင် ကိုယ်ပြချင်သည့် နာမည်ကို အစားထိုးပါ
            text = text.replace("@paing07709", "@paing07709 sout paw") 
            
        original_stdout.write(text)
        
    def flush(self):
        original_stdout.flush()

# Hook ကို စနစ်ထဲသို့ အစားထိုးထည့်သွင်းခြင်း
sys.stdout = OutputHook()


# =========================================================
# ၃။ မူရင်း Program (i.so) ကို စတင် Run ခြင်း
# =========================================================
if __name__ == "__main__":
    i.main()
