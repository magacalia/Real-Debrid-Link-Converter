import requests
from time import perf_counter

# Replace 'YOUR_API_KEY_HERE' with your actual Real Debrid API key
api_credentials = {'auth_token': 'YOUR_API_KEY_HERE'}

output_file_name = input('Output File Name: ')

start = perf_counter()
with open('episodes.txt') as input_file:
    with open(output_file_name, 'w') as output_file:

        total_episodes = len(input_file.readlines())
        input_file.seek(0)

        for index, episode in enumerate(input_file, start=1):
            r = requests.post('https://api.real-debrid.com/rest/1.0/unrestrict/link', data={'link': episode}, params=api_credentials)
            output_file.write(r.json()['download'] + '\n')
            print(f'[{index}/{total_episodes}] {r.json()['filename']}')
end = perf_counter()

print(f'Finished [{(end - start):.02f}s].')
