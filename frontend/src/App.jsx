
import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("Checking backend...");

  useEffect(() => {
    fetch("http://localhost:5000/api/health")
      .then((response) => response.json())
      .then((data) => setStatus(data.message))
      .catch(() => setStatus("Backend connection failed"));
  }, []);

  return (
    <div style={{ textAlign: "center", padding: "60px" }}>
      <h1>🌱 PlantCareAI</h1>
      <h2>AI-Powered Plant Health Assistant</h2>

      <p>Backend Status: {status}</p>
    </div>
  );
}

export default App;
