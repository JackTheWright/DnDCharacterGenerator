# DnDCharacterGenerator

This is a random character generator for the table top role-playing game
Dungeons and Dragons. It uses the Google Assistant Webhooks to send a custom
GET request to the generate page. This GET request contains the character
level.
A Python script then generates the character randomly and fills out the official
D&D character sheet PDF. This PDF is then hosted as a download on the website.

---

## TODO
1. Design a UI for the generator.
2. Finish the addition of randomized spells for each spellcasting class.
3. Fix the bug where the font does not scale with the text box size on the PDF.
4. Migrate Python lists to SQL Database.
