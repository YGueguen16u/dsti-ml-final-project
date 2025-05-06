// front_end/react_app/react_app_vite/src/components/ChatSection.tsx


import { useState, useRef, useEffect } from "react";
import { ChatMessage } from "../types/log";
import { ArrowRight } from "lucide-react";

interface ChatSectionProps {
  chatHistory: ChatMessage[];
  setChatHistory: (history: ChatMessage[]) => void;
}

const ChatSection = ({ chatHistory, setChatHistory }: ChatSectionProps) => {
  const [chatInput, setChatInput] = useState("");
  const containerRef = useRef<HTMLDivElement>(null);

  const handleSendMessage = () => {
    if (!chatInput.trim()) return;
    const msg = {
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      user_input: chatInput,
      input_type: "message",
      assistant_output: "(réponse simulée)"
    };
    setChatHistory([...chatHistory, msg]);
    setChatInput("");
  };

  // Scroll automatique en bas
  useEffect(() => {
    containerRef.current?.scrollTo({ top: containerRef.current.scrollHeight, behavior: "smooth" });
  }, [chatHistory]);

  return (
    <div className="border p-4 rounded-lg shadow bg-white mt-6">
      <h2 className="text-lg font-semibold mb-2">💬 Assistant</h2>

      <div
        className="max-h-64 overflow-y-auto bg-gray-50 p-3 border rounded space-y-2 text-sm"
        ref={containerRef}
      >
        {chatHistory.map((m, i) => (
          <div key={i}>
            <div className="text-right">
              <div className="inline-block bg-blue-500 text-white px-3 py-2 rounded-lg max-w-xs text-left">
                {m.user_input}
              </div>
            </div>
            <div className="text-left mt-1">
              <div className="inline-block bg-green-100 text-gray-800 px-3 py-2 rounded-lg max-w-xs">
                {m.assistant_output}
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="flex gap-2 mt-3">
        <input
          value={chatInput}
          onChange={(e) => setChatInput(e.target.value)}
          className="flex-1 p-2 border rounded"
          placeholder="Tapez un message..."
          onKeyDown={(e) => {
            if (e.key === "Enter") handleSendMessage();
          }}
        />
        <button
          onClick={handleSendMessage}
          className="bg-blue-600 text-white px-3 py-2 rounded flex items-center gap-1"
        >
          <ArrowRight size={18} />
        </button>
      </div>
    </div>
  );
};

export default ChatSection;