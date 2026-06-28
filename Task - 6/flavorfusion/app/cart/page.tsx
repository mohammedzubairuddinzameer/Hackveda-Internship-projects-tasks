"use client";

import { useCart } from "../context/CartContext";
import Navbar from "../components/Navbar";
import { useState } from "react";

export default function CartPage() {
  const { cart, increaseQty, decreaseQty, total, clearCart } = useCart();
  const [showModal, setShowModal] = useState(false);

  return (
    <main className="min-h-screen bg-gradient-to-br from-orange-100 via-red-100 to-yellow-100">

      {/* ✅ NAVBAR */}
      <Navbar />
      
      {/* 🔥 CONTENT */}
      <section className="px-6 pt-24 pb-10 max-w-7xl mx-auto animate-fadeIn ">

        {/* TITLE */}
        <h1 className="text-3xl font-bold text-red-600 mb-8">
          Your Cart 🛒
        </h1>

        {/* ❌ EMPTY CART */}
        {cart.length === 0 && (
          <div className="flex justify-center items-center mt-24 animate-fadeIn">
            <div className="bg-white p-8 rounded-xl shadow-lg text-center">
              <p className="text-xl font-semibold text-gray-700">
                Your cart is empty 😔
              </p>
              <p className="text-gray-500 mt-2">
                Please select items from menu
              </p>
            </div>
          </div>
        )}

        {/* ✅ CART CONTENT */}
        {cart.length > 0 && (
          <>
            {/* ITEMS */}
            <div className="space-y-5">
              {cart.map((item) => (
                <div
                  key={item.id}
                  className="flex items-center gap-4 bg-white p-4 rounded-xl shadow-md hover:shadow-xl hover:scale-[1.02] transition duration-300"
                >
                  {/* IMAGE */}
                  <img
                    src={item.image}
                    className="w-20 h-20 object-cover rounded-lg"
                    alt={item.title}
                  />

                  {/* DETAILS */}
                  <div className="flex-1">
                    <h2 className="font-semibold text-gray-800 text-lg">
                      {item.title}
                    </h2>
                    <p className="text-red-500 font-bold">
                      ₹ {item.price}
                    </p>
                  </div>

                  {/* QUANTITY */}
                  <div className="flex items-center gap-3 bg-gray-100 px-3 py-1 rounded-lg">
                    <button
                      onClick={() => decreaseQty(item.id)}
                      className="bg-red-500 text-white px-3 py-1 rounded hover:scale-110 active:scale-95 transition"
                    >
                      -
                    </button>

                    <span className="font-bold text-lg">
                      {item.quantity}
                    </span>

                    <button
                      onClick={() => increaseQty(item.id)}
                      className="bg-green-500 text-white px-3 py-1 rounded hover:scale-110 active:scale-95 transition"
                    >
                      +
                    </button>
                  </div>
                </div>
              ))}
            </div>

            {/* 💰 TOTAL SECTION */}
            <div className="mt-8 bg-white p-6 rounded-xl shadow-md animate-fadeIn">
              <h2 className="text-xl font-bold text-gray-800 mb-4">
                Total: ₹ {total}
              </h2>

              <div className="flex gap-4">
                {/* CHECKOUT */}
                <button
                  onClick={() => setShowModal(true)}
                  className="flex-1 bg-gradient-to-r from-orange-500 to-red-500 text-white py-3 rounded-lg font-semibold hover:scale-105 active:scale-95 transition"
                >
                  Checkout
                </button>

                {/* CLEAR */}
                <button
                  onClick={clearCart}
                  className="flex-1 bg-gray-300 text-gray-800 py-3 rounded-lg hover:bg-gray-400 transition"
                >
                  Clear
                </button>
              </div>
            </div>
          </>
        )}
      </section>

      {/* 🎉 MODAL */}
      {showModal && (
        <div className="fixed inset-0 bg-black/60 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded-xl text-center shadow-xl animate-scaleIn">

            <h2 className="text-lg font-bold mb-2 text-gray-800">
              Order Confirmed 🎉
            </h2>

            <p className="text-gray-600">
              Your food is being prepared!
            </p>

            <button
              onClick={() => {
                setShowModal(false);
                clearCart();
              }}
              className="mt-4 bg-orange-500 text-white px-4 py-2 rounded hover:bg-orange-600 transition"
            >
              Close
            </button>

          </div>
        </div>
      )}

    </main>
  );
}