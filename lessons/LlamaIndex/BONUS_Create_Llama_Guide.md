# 🌟 Bonus: Build a Professional Chat App in 60 Seconds

While Streamlit and Chainlit are great for prototyping, most professional AI apps are built with **React** and **Next.js**. LlamaIndex provides a powerful tool called `create-llama` that scaffolds a full-stack, production-ready application for you.

## 🚀 The Command
Open your terminal and run:

```bash
npx create-llama@latest
```

## 🛠 Recommended Choices
When the interactive menu appears, select these options for the best experience:

1.  **Project Name**: `my-ai-app`
2.  **Template**: `Chat with streaming` (provides the "typing" effect).
3.  **Framework**: `NextJS` (React).
4.  **Backend**: `Python` (to use the code you've learned in class).
5.  **UI**: `shadcn/ui` (gives you a beautiful, modern layout).
6.  **Data Source**: `Upload files` (you can add your own PDFs later).
7.  **Tools**: (Optional) Add `DuckDuckGo` if you want your bot to search the web!

## 🔗 Connecting Your Class Work
Once the project is created:

1.  **Add Your Key**: Copy your `OPENAI_API_KEY` into the `.env` file in your new project folder.
2.  **Add Your Data**: Drop any PDFs or TXT files from our class into the `/data` folder of your new project.
3.  **Generate the Index**: Run `npm run generate` in the terminal to process your files.
4.  **Start the App**: Run `npm run dev` and visit `http://localhost:3000`.

## 🎯 Why this is powerful
- **Streaming**: Tokens appear one by one, just like ChatGPT.
- **Responsive**: The app works perfectly on mobile phones.
- **Scalable**: This structure is ready to be deployed to **Vercel** or **Netlify** with one click.

---
*This is the "Pro Path" to GenAI development. If you've mastered the notebooks, this is your next step!*
