import hashlib
import sys
import os
import argparse
from concurrent.futures import ProcessPoolExecutor ,as_completed,wait ,FIRST_COMPLETED
import time
import random
    
    
def detect_hash(hash_value,mode):
    length = len(hash_value)
    if mode =="-d":

        if length == 32 : return [hashlib.md5],"MD5"
        if length == 40:  return[hashlib.sha1],"SHA1"
        if length == 64:   return [hashlib.sha256],"SHA256"
        if length ==  128:   return [hashlib.sha512],"SHA512"
        return None ,None
    elif mode == "-b" :
        return [hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha512],"all-algorithms"
    return None ,None

def check_password(password,target_hash,hash_algos):
    password = password.strip()
    for algo in hash_algos:
        if algo(password.encode()).hexdigest() ==target_hash.lower():
            return password
    return None

def worker(args_tuple):
    line,target_hash,algos =args_tuple
    return check_password(line,target_hash,algos)

#     
def main():
  
  #  os.system("cls" if os.name == "nt" else "clear")

    parser = argparse.ArgumentParser(description="Hash Cracker Tool crackx3",
                                     usage="%(prog)s [-d | -b] -hash <hash> -w <wordlist> [-h] or --help " ,
                                     
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog="""
Example:
    python3 crackx3.py -d -hash xws1r5... -w /usr/share/wordlists/rockyou.txt
    python3 crackx3.py -b -hash qef9o4... -w rockyou.txt
                                        """
                                     )
    parser.add_argument("-hash",required=True,help="target hash")
    parser.add_argument("-w",required=True,help="Wordlist path")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d",action="store_true",help="Detect Mode")
    group.add_argument("-b",action="store_true",help="Brute-force Mode")
    

    args = parser.parse_args()
    mode = "-d" if args.d else "-b"

    algos,algo_name = detect_hash(args.hash,mode)

    if not algos:
        print("[!] Invaled hash or mode use -b")
        return

    if not os.path.exists(args.w):
        print(f"[!] wordlist '{args.w}' not find....")
        return
    print("==========================================")    
    print("Welcome to crackx3 Tool")
    print("Created by x3bdulaziz")
    
    print(f"Starting crack... target: {args.hash}")
    print(f"Mode: {mode} | Algorithm: {algo_name}")
    print("==========================================")
    start = time.time()
    with open(args.w,"r",encoding="utf-8", errors="ignore") as f :
        try:
      
            with ProcessPoolExecutor() as executor:
                batch_size =5000
                futures ={}
                def fill_batch():  
                    count = 0
                    for line in f:
                        line = line.strip()
                        if line:
                            fut = executor.submit(worker,(line,args.hash,algos))
                            futures[fut] = line
                            count +=1
                        if count >= batch_size:break
                    return count
                fill_batch()
                while futures:
                    done,_= wait(futures,return_when=FIRST_COMPLETED)
                    for future in done:
                        result = future.result()
                        if result:
                        
                            end = time.time()
                            print(f"\n[+]Password Found: `{result}`")
                            print(f"finished in {end - start :.2f}seconds. ")
                            executor.shutdown(wait=False)
                            return
                        del futures[future]
                    fill_batch()
            print("\n[-] Password not found..")
        except  KeyboardInterrupt:
            executor.shutdown(wait=False,cancel_futures=True)
            print("\n user stoped the process..")

            os._exit(0)
           
            
        except Exception as e:
            executor.shutdown(wait=False,cancel_futures=True)
            print(f"on error occurred {e}")
            
           
            os._exit(0)



        


if __name__ == "__main__":
    main()