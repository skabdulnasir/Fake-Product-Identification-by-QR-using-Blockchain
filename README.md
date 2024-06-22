# Fake-Product-Identification-by-QR-using-Blockchain
With the dynamics of a rapidly globalizing and evolving technological world, the increase in fake products has become a prominent threat to both businesses and consumers. Objective of our project, is to eliminate this issue completely by using blockchain which is immutable and decentralized. We store crucial product data like product id, name, timestamp of addition, company name and address etc. in blockchain and develop a tamper-proof, verifiable digital ledger. Our model is centered on generating a single QR code for a specific product. This QR code captures a SHA-256 hash and a digital signature that prove the integrity of the data and protect it from manipulation. The digital signature authenticates the product details, while the SHA-256 hashing algorithm provides a robust mechanism for securing the data. Additionally, we enhance the QR code's security and brand recognition by embedding a watermark of the company name and a distinctive border. In order to make it more convenient for everyone to verify with the product, we developed a QR scan system that can scan the QR code and read the relevant data from the blockchain. The app then scans the QR Code, validates the digital signature, and compares the scanned data to the record saved in the blockchain. The accuracy check makes sure that someone off the street can look at a product and directly be able to identify both genuine and counterfeit products. Our solution improves consumer confidence, and brand reputation, whilst delivering an industry leading product validation system. By marrying blockchain technology with QR codes and state-of-the-art cryptographic tools, we have created a trustworthy and flexible mechanism to fight against counterfeiting across a multitude of domains.

## Built With <a name="built_with"></a>
GUI App:
+ [Python GUI](https://docs.python.org/3/library/tkinter.html) - GUI app
+ [MySQL](https://pypi.org/project/pymysql/) - Database for login/register
+ [qrcode](https://pypi.org/project/qrcode/) ,[pyzbar](https://pypi.org/project/pyzbar/) - creating and reading a dynamic QR code
+ [Tools] - VS code
  

Blockchain:
+ [Blockchain in python](https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/) - Pre-built Runtime



## Limitations <a name="limitations"></a>
+ The user needs to have a QR code scanner in order to check the product information.
+ Products that have already been manufactured prior to today cannot be tracked.
+ We currently depend on the company to register with our services, without which, we cannot provide information about a brand to the user.

## Future Scope <a name="future_scope"></a>
+ Making an Android app on this architecture 
+ To track every genuine product that is to be sold.
+ Implement this idea in other fields.
+ Virtual transactions
+ Using tamper-proof tags
+ Dynamic (read & write NFC tags)
+ Implement our own tokens which can be sold to users so that they can purchase ownership of a product using tokens that helps in insurance processing.
+ Integrating machine learning algorithms to predict and identify potential counterfeit patterns proactively
+ One of the immediate extensions could be the implementation of a more decentralized and scalable blockchain network, possibly integrating with established blockchain platforms such as Ethereum or Hyperledger 
