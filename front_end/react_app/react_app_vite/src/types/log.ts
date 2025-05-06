
export interface FoodItem {
  name: string;
  quantity: string;
  calories: number;
  protein: number;
  fat: number;
  carbs: number;
}

export interface Meal {
  name: string;
  items: FoodItem[];
  total_nutrients: {
    calories: number;
    protein: number;
    fat: number;
    carbs: number;
  };
}

export interface Activity {
  type: string;
  [key: string]: any;
}

export interface ChatMessage {
  time: string;
  user_input: string;
  input_type: string;
  assistant_output: string;
}
