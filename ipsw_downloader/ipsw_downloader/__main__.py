from tqdm import tqdm
import os
import connection
import devicetypes
import interface


def create_folder(name="IPSWs", no_sync=True):
    dir_name = name
    if no_sync == True:
        dir_name = name + ".nosync"
    desktop = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop", "")
    path = os.path.join(desktop, dir_name, "")
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def download(session, device, name):
    path = create_folder()
    target_url = session.get("http://api.ipsw.me/v2.1/{}/latest/url".format(device))
    r = session.get(target_url.text, stream=True)
    print("\nDownloading {} IPSW from:\n {}\n".format(name, target_url.text))
    total_size = int(r.headers.get("content-length", 0))
    block_size = 1024
    t = tqdm(
        total=total_size, desc=name, unit="iB", unit_scale=True, position=0, leave=True
    )
    with open("{}{}.ipsw".format(path, name), "wb") as f:
        for data in r.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    if total_size != 0 and t.n != total_size:
        print("ERROR, something went wrong")


def main():

    session = connection.session_with_retry(retries=20, backoff_factor=0.5)
    devices = interface.user_interface()

    payload = devicetypes.create_payload(devices)

    for i in payload:
        device, name = i[0], i[1]
        download(session, device, name)


if __name__ == "__main__":
    main()
