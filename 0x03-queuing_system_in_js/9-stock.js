const express = require('express');
const redis = require('redis');
const util = require('util');
const app = express();
const port = 1245;

// Sample product list
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Initialize Redis client
const client = redis.createClient();
client.get = util.promisify(client.get);
client.set = util.promisify(client.set);

// Helper function to get product by ID
function getItemById(id) {
  return listProducts.find(product => product.id === id);
}

// Reserve stock in Redis
async function reserveStockById(itemId, stock) {
  await client.set(`item:${itemId}`, stock);
}

// Get current reserved stock
async function getCurrentReservedStockById(itemId) {
  const reservedStock = await client.get(`item:${itemId}`);
  return reservedStock ? parseInt(reservedStock, 10) : 0;
}

app.get('/list_products', (req, res) => {
  const products = listProducts.map(product => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock
  }));
  res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(parseInt(req.params.itemId, 10));
  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(item.id);
  res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: item.stock - reservedStock
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  if (reservedStock >= item.stock) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  await reserveStockById(itemId, reservedStock + 1); // Reserve one item
  res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
