# NFT Analytics

The scripts in this repo were written in Python to capture the following data points using [QuickNode's endpoint](https://dashboard.quicknode.com/endpoints/new/ETH/mainnet) and [QuickNode's Marketplace Blockspan add-on](https://marketplace.quicknode.com/add-on/nft-api-with-cached-metadata):

- NFT floor prices
- NFT top collections
- NFT Sales (by marketplace)

## Setting up your Endpoint

Setting up your Ethereum endpoint with [QuickNode's Marketplace Blockspan add-on](https://marketplace.quicknode.com/add-on/nft-api-with-cached-metadata) is quite easy:

- If you haven't signed up already, you can create an account [here](https://www.quicknode.com/signup).

- Once you have logged in, navigate to the [Endpoints](https://www.quicknode.com/endpoints) page and click **Create an endpoint**. Select **Ethereum mainnet**, then click Next. Then, you'll be prompted to configure the add-on. Activate **NFT API With Cached Metadata by BlockSpan**. Afterward, simply click **Create Endpoint**.

To fetch your `blockspan_key` navigate to the **Add-ons** page within your Ethereum endpoint, go to the **NFT API With Cached Metadata by BlockSpan** section, and click on the `Dashboard` drop-down. This will take you to our partner's Blockspan portal, for which their service is natively integrated with our nodes globally. 

Make sure to put your `blockspan_key` in your `.env` file before running the scripts. 
