# opnlend
**_*Note: This is far from being a finished product. The initial app pipeline is the core funcitonality: relationships (affiliates), loans, and spreading.*_**

**_A framework for an open source, modular commercial and government guaranteed (SBA and USDA) loan origination system. The intent of this project is an "ala carte" approach. Each app is to be individually installed to the individual or institution's needs (Loans, Deposits, Collateral, Spreading, Profiles, etc.). Furthermore, it is to be locally hosted; mitigating risk of downtime when compared to a 3rd party cloud server. I am currently developing this within a Proxmox container (LXC) hosted on my home server, integrated with my PostgreSQL database hosted in a separate LXC._**

![opnlend-logo-banner](media/images/opnlend-logo-banner.jpg)

**Introduction**

I'm in the very beginning stages, including planning and design. While I have been working in commercial credit/underwriting for the last decade, I'm still a beginner at coding outside of VBA. I have experience utilizing various different loan origination systems (Fusion Credit Quest, Abrigo Sageworks, nCino, and others), collaborated with LOS engineers when improving financial institutions' existing integrations, and developed various auto filled templates to improve efficiencies. During downtime at my last job, I coded a VBA-based Commercial Loan Review, Underwriting, and Spreadsheet application within Excel. However, due to it being Excel, it came with limitations imposed by the host hardware (institution issued laptop) that could ultimately be overcome through a web-based (hosted) application.

I'm more so using this application as a learning project to continue learning coding while applying my professional commercial credit experience. I'm using ChatGPT-4 to assist with the backend coding and debugging. **_Also, I'll almost certainly have to halt future development of this upon beginning my next job due to likely having to sign Intellectual Property Assignment contracts. In the meantime, it keeps my credit skillset sharp while adding additional skills (Python and PostgreSQL)._** I've uploaded it here in hopes that someone else may express interest in it. Or, if developed further, could be used as an educational tool for those in university.

I've uploaded some initial models.py files to the /loans and /relationships folder, though much remains to be added to both. Many of the initial loan's model.py were created with the SBA's Form 1920 in mind, allowing for automated population of the form later down the road. I've also uploaded a Financial Spreading Model that I created in Excel. While I could embed it as the spreadsheet solution to this application, I think there are better options. I'm more so uploading it as an example.

I'll update this readme soon to reflect initial project goals and features that are to be added.
