import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.io.File;

public class Edit {

    public static void editJMX(String xmlfile,String time){
        try {
            File fXmlFile = new File(xmlfile);
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document doc = dBuilder.parse(fXmlFile);
            doc.getDocumentElement().normalize();

            System.out.println("Root element :" + doc.getDocumentElement().getNodeName());

            //NodeList nList = doc.getElementsByTagName("hashTree");

            // For Thread Group
            NodeList tList = doc.getElementsByTagName("ThreadGroup");


            for (int tem = 0; tem < tList.getLength(); tem++) {
                Node tNode = tList.item(tem);
                if (tNode.getNodeType() == Node.ELEMENT_NODE) {
                    Element eElement = (Element) tNode;
                    System.out.println("Node Element :" + tNode.getNodeName());
//                    System.out.println("Start time value : " + eElement.getElementsByTagName("longProp").item(0).getTextContent());
                    Node timer = eElement.getElementsByTagName("longProp").item(0);
                    timer.setTextContent(time);
                    System.out.println("Start time value : " + eElement.getElementsByTagName("longProp").item(0).getTextContent());
                    //break;
                }
            }


            // write the content into xml file
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource source = new DOMSource(doc);
            StreamResult result = new StreamResult(new File(xmlfile));
            transformer.transform(source, result);


        } catch (Exception exec) {
            System.out.println(exec);
        }
    }


}
