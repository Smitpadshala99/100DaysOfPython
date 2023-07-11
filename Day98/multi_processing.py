import multiprocessing as mp
import requests

def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished downloading {name}")


if __name__ == '__main__':
    url = "https://picsum.photos/2000/3000"
    processes = []
    for i in range(5):
        p = mp.Process(target=downloadFile, args=(url, i))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
