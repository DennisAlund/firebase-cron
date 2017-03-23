# Firebase Cloud Function scheduler
This is a simple cron/scheduler for Firebase Cloud Functions as described in
[an article that I wrote on the topic](https://medium.com/evenbit/d031994618d9).

## Firebase deploy key
Extract a Firebase deploy key for non-interactive environments by running

```
$ firebase login:ci
```
And follow the instructions in your web browser.

## Cron API key
Set the API key to whatever you want. For simplicity sake, you can use [random.org](https://www.random.org/) 
to [get a random key](https://www.random.org/strings/?num=1&len=20&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd=new). 

The key must be replaced in [app.yaml](app-engine/app.yaml):
```
$ sed -i s/{CRON_API_KEY}/YourSecretApiKey/ app-engine/app.yaml
```
# Deploy with Travis CI
The project is ready to be deployed with Travis CI. You just need to set the 
build configuration variables `FIREBASE_DEPLOY_KEY` and `CRON_API_KEY` as described above.

With a little bit of magic you can also deploy your App Engine project from Travis and that
also brings the benefits of making sure that the API key is automatically injected into your 
App Engine configuration in the same process as it is configured for your Firebase project.
