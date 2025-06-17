import os
import sys
import subprocess

def main():
    """Executa a detecção de código duplicado em todo o projeto."""
    # Diretórios a serem verificados
    dirs_to_check = ["mysite/acervo", "mysite/enquetes", "mysite/mysite"]
    
    min_similarity_lines = 3  # Reduzindo para 3 linhas similares
    
    found_duplicates = False
    
    for directory in dirs_to_check:
        if not os.path.exists(directory):
            print(f"Diretório {directory} não encontrado. Pulando...")
            continue
            
        print(f"\nVerificando código duplicado em: {directory}")
        print("=" * 80)
        
        try:
            # Executa pylint com o módulo de similaridades
            cmd = [
                "pylint", 
                "--disable=all", 
                "--enable=duplicate-code", 
                "--min-similarity-lines", str(min_similarity_lines),
                directory
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.stdout.strip():
                print(result.stdout)
                
                # Verifica se encontrou duplicações
                if "Similar lines in" in result.stdout:
                    found_duplicates = True
            else:
                print("Nenhum código duplicado encontrado!")
                
            if result.stderr.strip():
                print("ERROS:", result.stderr)
                
        except Exception as e:
            print(f"Erro ao verificar duplicações: {e}")
            return 1
    
    # Retorna 1 se encontrou duplicações
    return 1 if found_duplicates else 0

if __name__ == "__main__":
    sys.exit(main())