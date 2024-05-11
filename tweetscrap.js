const Twit = require('twit'); // Assuming you have Node.js with npm or yarn

const config = {
    consumer_key: 'your_consumer_key',
    consumer_secret: 'your_consumer_secret',
    access_token: 'your_access_token',
    access_token_secret: 'your_access_token_secret'
};

const T = new Twit(config);

async function getTweets(hashtag, limit, lang, beginDate, endDate) {
    try {
        const response = await T.get('search/tweets', {
            q: hashtag,
            count: limit,
            lang: lang,
            since: beginDate, // Format: YYYY-MM-DD
            until: endDate   // Format: YYYY-MM-DD
        });

        const tweetsData = response.data.statuses.map(tweet => ({
            screen_name: tweet.user.screen_name,
            username: tweet.user.name,
            text: tweet.text,
            hashtags: tweet.entities.hashtags.map(hashtag => hashtag.text)
        }));

        return tweetsData;
    } catch (error) {
        console.error(error);
        return []; // Handle errors gracefully
    }
}

// Example usage (assuming you have a button to trigger the scraping):
const button = document.getElementById('scrape-button');
button.addEventListener('click', async () => {
    const hashtag = document.getElementById('hashtag-input').value;
    const limit = parseInt(document.getElementById('limit-input').value);
    const lang = document.getElementById('lang-input').value;
    const beginDate = document.getElementById('begin-date-input').value;
    const endDate = document.getElementById('end-date-input').value;

    const tweets = await getTweets(hashtag, limit, lang, beginDate, endDate);
    console.log(tweets); // Process and potentially display the tweets
});
