
const express = require("express");
const cors = require("cors");

const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

// Test route
app.get("/", (req, res) => {
    res.send("PlantCareAI Backend is running!");
});

// Health check API
app.get("/api/health", (req, res) => {
    res.json({
        status: "success",
        message: "PlantCareAI API is working!"
    });
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
