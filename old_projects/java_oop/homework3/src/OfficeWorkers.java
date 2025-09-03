import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class OfficeWorkers implements Iterator {
    private List office = new ArrayList<>();

    public OfficeWorkers() {
        office = new ArrayList<Object>();
    }


    public List getOffice() {
        return office;
    }

    public void addNewWorker(Object object){
        office.add(object);
    }


    int index;
    @Override
    public boolean hasNext() {
        return index < office.size();
    }

    @Override
    public Object next() {
        return office.get(index++);
    }
}
