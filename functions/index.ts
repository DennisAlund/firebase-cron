export const cronEndpoint = functions.https.onRequest((request, response) => {
    if (functions.config().cron.apikey !== request.body.key) {
        response.status(401).send("I'm sorry Dave, I'm afraid I can't do that");
        return;
    }

    response.status(200).send("Hello World");
});
