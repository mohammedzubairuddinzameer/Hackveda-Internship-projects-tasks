const express = require("express");
const router = express.Router();
const Order = require("../models/Order");

// POST /api/orders
router.post("/", async (req, res) => {
  try {
    const { items, totalAmount } = req.body;

    if (!items || items.length === 0) {
      return res.status(400).json({ message: "No items in order" });
    }

    const newOrder = new Order({
      items,
      totalAmount,
    });

    const savedOrder = await newOrder.save();

    res.status(201).json({
      message: "Order saved successfully",
      orderId: savedOrder._id,
    });
  } catch (error) {
    res.status(500).json({
      message: "Failed to save order",
      error: error.message,
    });
  }
});

module.exports = router;