export const nxSyncRequest = functions.https.onRequest(async(request, response) => {
    if (functions.config().cron.apiKey !== request.body.key) {
        response.status(401).send("I'm sorry Dave, I'm afraid I can't do that");
        return;
    }

    response.status(200).send("Hello World");
});
