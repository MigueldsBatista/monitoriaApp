from dotenv import load_dotenv
import os


load_dotenv()

chave_secreta=os.getenv('CHAVE_SECRETA')

print(chave_secreta)