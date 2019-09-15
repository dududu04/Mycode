import gevent
import urllib.request

def downloader(img_name, img_url):
	req = urllib.request.urlopen(img_url)

	img_content = req.read()

	with open(img_name, "wb") as f:
		f.write(img_content)

def main():
	gevent.joinall([
		gevent.spawn(downloader, "1.jpg", "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1568471902937&di=d5cdfece4a51a2513080491e392ab9d6&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201810%2F29%2F20181029234752_qaysj.thumb.700_0.jpg"),
		gevent.spawn(downloader, "2.jpg", "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1569066566&di=3dade2092455e72fb795847f4c9ddfed&imgtype=jpg&er=1&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201806%2F30%2F20180630142310_illni.jpg"),
		gevent.spawn(downloader, "3.jpg", "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1568471521619&di=62774803642bcdd260202b84ead2ea4a&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201810%2F30%2F20181030212754_mglbs.thumb.700_0.jpg")
	])


if __name__ == "__main__":
	main()
