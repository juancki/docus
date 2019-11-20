gcloud compute instances create \
  --image-family ubuntu-1804-lts \
  --image-project ubuntu-os-cloud \
  --machine-type n1-standard-4 \
  --boot-disk-size=200 \
  --boot-disk-type=pd-ssd \
  --metadata-from-file user-data=chromoting.cloud-init \
  desktop-$1
