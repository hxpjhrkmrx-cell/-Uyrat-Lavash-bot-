async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'menu':
        await menu(update, context)
    elif query.data == 'contact':
        await contact(update, context)
    elif query.data == 'info':
        await query.edit_message_text("ℹ️ *Uyrat Lavash - Rishton tumanidagi eng yaxshi lavash!*", parse_mode='Markdown')
    elif query.data == 'home':
        await start(update, context)

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 Bot ishga tushdi...")
    app.run_polling()

if name == 'main':
    main()
