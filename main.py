#Analisador de Logs de Servidor

from flask import Flask, render_template, request
import re

# Regex : (?<IP>(\d{1,3}\.){3}\d{1,3})\s(?<userInfo>-.-)\s\[(?<Date>\d{2}\/\w{1,4}\/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4})\]\s\"(?<Log>.*)\"\s(?<statuscode>\d{1,3})\s(?<PacketSize>\d*)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_logs', methods=['GET', 'POST'])
def upload_logs():
    if request.method == 'POST':
        log_file = request.files['logFile']
        logs = log_file.read().decode('utf-8')

        log_pattern = r'(?P<IP>(\d{1,3}\.){3}\d{1,3})\s(?P<userInfo>-.-)\s\[(?P<Date>\d{2}\/\w{1,4}\/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4})\]\s\"(?P<Log>(?P<RequestType>\w*))\s\/(?P<Page>\w*)\s.*\"\s(?P<statuscode>\d{1,3})\s(?P<PacketSize>\d*)'
        logs_match = re.finditer(log_pattern, logs)

        # Converter logs_match em uma lista para evitar consumir o iterador
        logs_list = list(logs_match)

        # Processar logs e gerar estatísticas

        # Calcular Top 10 IPs
        ip_count = {}
        for match in logs_list:
            ip = match.group('IP')
            ip_count[ip] = ip_count.get(ip, 0) + 1

        top_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:10]

        # Calcular Códigos de Status
        status_codes = {}
        for match in logs_list:
            status_code = match.group('statuscode')
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

        # Calcular Estatísticas de Tamanho de Pacotes
        packet_sizes = [int(match.group('PacketSize')) for match in logs_list if match.group('PacketSize').isdigit()]
        min_packet_size = min(packet_sizes) if packet_sizes else 0
        max_packet_size = max(packet_sizes) if packet_sizes else 0
        avg_packet_size = sum(packet_sizes) / len(packet_sizes) if len(packet_sizes) > 0 else 0

        # Calcular Top 10 Páginas Mais Acessadas
        page_count = {}
        for match in logs_list:
            request_type = match.group('RequestType')
            page = match.group('Page')
            page_count[(request_type, page)] = page_count.get((request_type, page), 0) + 1

        top_pages = sorted(page_count.items(), key=lambda x: x[1], reverse=True)[:10]

        return render_template('results.html', 
                               top_ips=top_ips,
                               status_codes=status_codes.items(),
                               min_packet_size=min_packet_size,
                               max_packet_size=max_packet_size,
                               avg_packet_size=avg_packet_size,
                               top_pages=top_pages,
                               # Adicione outras variáveis conforme necessário
                               )



if __name__ == '__main__':
    app.run(debug=True)
