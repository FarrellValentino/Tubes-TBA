import sys

class HTMLParser:
    def __init__(self):
        self.stack = []

    def is_valid_html(self, html):
        self.stack = [] 
        i = 0
        while i < len(html):
            if html[i] == '<':
                j = i + 1
                while j < len(html) and html[j] != '>':
                    j += 1
                if j == len(html):
                    return False  # Invalid tag

                tag = html[i + 1:j]
                if tag[0] != '/':
                    self.stack.append(tag)
                else:
                    if not self.stack or self.stack[-1] != tag[1:]:
                        return False
                    self.stack.pop()
                i = j
            i += 1
        return len(self.stack) == 0

    def is_valid_html_structure(self, html): #memeriksa struktur dokumen HTML untuk memastikan elemen-elemen dasar ada dan berurutan dengan benar.
        if not self.is_valid_html(html): # memastikan bahwa tag HTML berpasangan dengan benar
            return False
        if '<html>' not in html or '</html>' not in html: #Memeriksa apakah tag pembuka <html> dan tag penutup </html> ada di dalam string html
            return False
        head_start = html.find('<head>')
        head_end = html.find('</head>')
        body_start = html.find('<body>')
        body_end = html.find('</body>') #Mencari posisi awal dan akhir dari tag <head> dan </head>, serta <body> dan </body>, dalam string html

        if head_start != -1 and (head_end == -1 or head_end < head_start):
            return False #Memeriksa apakah tag <head> ada tanpa tag penutup </head> yang benar atau urutan tag <head> salah
        if body_start != -1 and (body_end == -1 or body_end < body_start):
            return False #Mengecek kaklau tanda tag body ada tanpa tag penutup /body yang benar atau urutan tag body salah
        if head_end != -1 and body_start != -1 and head_end > body_start:
            return False #Memeriksa apakah urutan tag <head> dan <body> tidak tumpang tindih.

        return True

if __name__ == "__main__":
    if len(sys.argv) < 2: #Memeriksa apakah jumlah argumen baris perintah kurang dari 2
        print("Usage: python program.py input.html")
        sys.exit(1) #Jika ya, mencetak pesan penggunaan dan keluar dari program dengan kode status 1.


    input_file = sys.argv[1] #Mendapatkan nama file dari argumen baris perintah.
    with open(input_file, 'r') as file:
        html = file.read() #Membuka file dengan nama yang diberikan dalam mode baca ('r') dan membaca seluruh kontennya ke dalam variabel html.

    parser = HTMLParser() #Membuat instance dari kelas HTMLParser.
    result = parser.is_valid_html_structure(html)  #memanggil fungsi is valid structure
    print(f"Input file {input_file}: {'Accepted' if result else 'Rejected'}")  #output acc kl struktur HTML valid, rejected kl ga valid
