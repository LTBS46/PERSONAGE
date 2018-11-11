
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder
import javax.xml.parsers.ParserConfigurationException;
import java.io.File;
import org.w3c.dom.Document;
import java.io.IOException;
import org.xml.sax.SAXException;

final DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
		try {
final DocumenetBuilder = factory.newDocumentBuilder();
final Document document= builder.parse(new File("../xml/A.xml"));
		}
		catch (final ParserConfigurationException e) {
		e.printStackTrace();
		}
		catch (final SAXException e) {
		e.printStackTrace();
		}
		catch (final IOException e) {
		e.printStackTrace
		}
		System.out.println(document.getXmlVersion());
		System.out.println(document.getXmlEncoding());
		System.out.println(document.getXmlStandalone());