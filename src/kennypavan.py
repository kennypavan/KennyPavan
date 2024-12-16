class kennypavan:
	def __init__(self):
		self.name = "Kenny Pavan"
		self.email = "kennypavan@protonmail.com"
		self.github = "https://github.com/kennypavan/"
		self.linkedin = "https://www.linkedin.com/in/kennypavan/"
		self.website = "https://www.kennypavan.com/"
		self.bluesky = "https://bsky.app/profile/kennypavan.com"
		self.instagram = "https://www.instagram.com/kennypavan/"

	def about(self):
		output = """Experienced Software Developer with a demonstrated history of 
				working in the computer software industry. Skilled in Python, Java, C
				++, Javascript, PHP (Laravel), Linux, SQL, and Computational Biology. 
				Strong engineering professional with multiple bachelor degrees. Currently
				leveraging machine learning, graph convolutional neural networks, and 
				various computational strategies to unravel complex biological systems, 
				particularly in single cell and spatial analyses."""
		return output

	def education(self):
		output = "PhD. Biomedical Engineering, Oregon Health and Science University (expected 2026)\n"
		output += "B.S. Computer Science, Western Governors University\n"
		output += "B.S. Molecular Biology, Montclair State University\n"
		output += "B.A. Digital Communication and Media/Multimedia, Ramapo College\n"
		return output

	def skills(self):
		output = "Python\n"
		output += "JavaScript\n"
		output += "C++\n"
		output += "Java\n"
		output += "PHP (Laravel)\n"
		output += "HTML/CSS\n"
		output += "SQL (various flavors)\n"
		output += "Machine learning\n"
		output += "Data visualization\n"
		output += "Web development\n"
		output += "Bioinformatics\n"
		output += "Single-cell Analysis\n"
		output += "Spatial Analysis\n"
		output += "Platform Development\n"
		return output

	def experience(self):
		output = "Oregon Health & Science University\n"
		output += "- Biomedical Engineering PhD Candidate: Developing high-throughput analysis packages to understand synaptic connectivity.\n"
		output += "aDNATool\n"
		output += "- Founder & Bioinformatics Developer: Built an elastic platform for RNA-Seq analysis (2021-2022).\n\n"
		output += "Self-Employed (Software Development)\n"
		output += "- Full-Stack Engineer & Consultant: Developed cloud-based inventory and blockchain projects (2019-2022).\n\n"
		output += "Anchor Digital, Inc.\n"
		output += "- Senior Database & Backend Developer: Built an institutional trading platform using blockchain (2017-2020).\n\n"
		output += "Xy Web Solutions\n"
		output += "- Founder & Lead Developer: Managed a team of six to deliver eCommerce platforms, iOS apps, and operational tools (2009-2015).\n"
		return output

	def publications(self):
		output = "Publications:\n"
		output += "- 'AnnSQL: A Scalable SQL Interface for Single-Cell Data'\n"
		output += "  Authors: Kenny Pavan, Arpiar Saunders.\n"
		output += "  DOI: https://doi.org/10.1101/2024.11.02.621676\n"
		output += "  Description: This publication introduces AnnSQL, a novel package enabling SQL-based interaction with AnnData objects. The tool streamlines single-cell data processing and supports efficient querying of large-scale datasets."
		return output
