until sudo python run.py; do
    echo "Whatsapp bot crashed with code $?.  Respawning.." >&2
    sleep 1
done