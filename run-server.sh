nohup python server/server.py >/dev/null 2>&1 &
sleep 1
echo "running tail > flask server"
tail /tmp/hearthstone-redirected.log --follow | python server/proxy.py
