const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

// Initialize Express app
const app = express();
const port = 1245;

// Create Redis client
const client = redis.createClient();

// Promisify the get function
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.get).bind(client);

client.on('error', (err) => {
  console.error('Error connecting to Redis', err);
});

// List of products
const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5
  },
];
// Function to get item by ID
function getItemById(id) {
  return listProducts.find(product => product.itemId === id);
}

// Function to reserve stock by item ID
function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock, redis.print);
}

// Async function to get the current reserved stock by item ID
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

// Route to get list of products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route to get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = currentStock !== null ? parseInt(currentStock, 10) : product.initialAvailableQuantity;

  res.json({
    ...product,
    currentQuantity
  });
});

// Route to reserve a product by ID
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = currentStock !== null ? parseInt(currentStock, 10) : product.initialAvailableQuantity;

  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  await reserveStockById(itemId, currentQuantity - 1);

  res.json({ status: 'Reservation confirmed', itemId });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
