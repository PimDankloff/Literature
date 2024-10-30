import bibtexparser
import pyperclip


def bibtex_to_markdown(bibtex_entry):
    # Parse the BibTeX entry
    bib_database = bibtexparser.loads(bibtex_entry)
    entry = bib_database.entries[0]

    # Extract relevant fields
    authors = entry["author"].replace(" and ", "; ")
    title = entry["title"]
    journal = entry["journal"]
    volume = entry.get("volume", "")
    number = entry.get("number", "")
    pages = entry.get("pages", "")
    year = entry["year"]
    publisher = entry.get("publisher", "")
    url = entry["url"]

    # Format the volume and number
    volume_number = f"**{volume}**" + (f"({number})" if number else "")

    # Construct the Markdown citation
    citation = f"- [{title}]({url}). {authors}. *{journal}* {volume_number}, {pages}. {publisher}, {year}."
    pyperclip.copy(citation)


# Example usage
bibtex_entry = """

@article{nnadili_surfactant-specific_2024,
	title = {Surfactant-{Specific} {AI}-{Driven} {Molecular} {Design}: {Integrating} {Generative} {Models}, {Predictive} {Modeling}, and {Reinforcement} {Learning} for {Tailored} {Surfactant} {Synthesis}},
	volume = {63},
	issn = {0888-5885},
	shorttitle = {Surfactant-{Specific} {AI}-{Driven} {Molecular} {Design}},
	url = {https://doi.org/10.1021/acs.iecr.4c00401},
	doi = {10.1021/acs.iecr.4c00401},
	abstract = {Molecular design is a critical aspect of various scientific and industrial fields, where the properties of molecules hold significant importance. In this study, a 3-fold methodology design is presented that leverages the power of generative artificial intelligence (AI), predictive modeling, and reinforcement learning to create tailored molecules with desired properties. This model synergistically combines deep learning techniques with Self-Referencing Embedded Strings (SELFIES) molecular representation to build a generative model that generates valid molecules and a graphical neural network model that accurately forecasts molecular properties. The Variational Autoencoder (VAE) coupled with reinforcement learning helps refine molecule generation based on targeted attributes. Data from an experimental study involving surfactants were used to test the framework. A validation of the structural integrity of the molecules generated was conducted, and Tanimoto similarities were used to quantify the similarity and diversity between the original and generated molecular structures. Also, saliency maps for the generated surfactants were produced to identify the features explaining the property values. Lastly, molecular dynamics simulations were used to validate the stability of the generated molecules. The results showed that the proposed framework can effectively produce valid molecules within the set property threshold value.},
	number = {14},
	urldate = {2024-08-05},
	journal = {Industrial \& Engineering Chemistry Research},
	author = {Nnadili, Miriam and Okafor, Andrew N. and Olayiwola, Teslim and Akinpelu, David and Kumar, Revati and Romagnoli, Jose A.},
	month = apr,
	year = {2024},
	note = {Publisher: American Chemical Society},
	pages = {6313--6324},
	file = {Nnadili et al_2024_Surfactant-Specific AI-Driven Molecular Design.pdf:C\:\\Users\\pimda\\Zotero\\storage\\8SIMF5G6\\Nnadili et al_2024_Surfactant-Specific AI-Driven Molecular Design.pdf:application/pdf},
}

"""

# Convert and copy the md citation to clipboard
bibtex_to_markdown(bibtex_entry)
