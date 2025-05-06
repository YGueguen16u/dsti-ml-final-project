// front_end/react_app/react_app_vite/src/components/ChatSection.tsx


import { useState } from "react";
import { ChatMessage } from "../types/log";

interface ChatSectionProps {
  chatHistory: ChatMessage[];
  setChatHistory: (history: ChatMessage[]) => void;
}

const ChatSection = ({ chatHistory, setChatHistory }: ChatSectionProps) => {
  const [chatInput, setChatInput] = useState("");

  const handleSendMessage = () => {
    const msg = {
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      user_input: chatInput,
      input_type: "message",
      assistant_output: "(réponse simulée)"
    };
    setChatHistory([...chatHistory, msg]);
    setChatInput("");
  };

  return (
    <div>
      <h2 className="text-lg font-semibold">Assistant</h2>
      <div className="max-h-60 overflow-y-auto bg-gray-100 p-2 border mb-2">
        {chatHistory.map((m, i) => (
          <div key={i} className="mb-2">
            <div className="text-right text-blue-700">Vous: {m.user_input}</div>
            <div className="text-left text-green-700">Coach: {m.assistant_output}</div>
          </div>
        ))}
      </div>
      <div className="flex gap-2">
        <input value={chatInput} onChange={(e) => setChatInput(e.target.value)} className="flex-1 p-2 border rounded" />
        <button onClick={handleSendMessage} className="bg-green-600 text-white px-3 py-1 rounded">Envoyer</button>
      </div>
    </div>
  );
};

export default ChatSection;
