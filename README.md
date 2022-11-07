
# Data-Mining(作業一)

姓名：侯則瑜

學號：p77091106

### Command line example (1)

```
##  apriori
python main.py --method apriori --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.1 --min_conf 0.1
python main.py --method apriori --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.1 --min_conf 0.6
python main.py --method apriori --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.3 --min_conf 0.1
python main.py --method apriori --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.3 --min_conf 0.6

##  fptree
python main.py --method fptree --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.1 --min_conf 0.1
python main.py --method fptree --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.1 --min_conf 0.6
python main.py --method fptree --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.3 --min_conf 0.1
python main.py --method fptree --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.3 --min_conf 0.6
```

### Command line example (2)

Edit the `run.sh` file, then `sh run.sh`.

### Output

Store the support and confidence to `outputs` folder.

###  History

```
ython main.py --method fptree --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.1 --min_conf 0.1
method: fptree
31.59 sec
find 1495 item set
confidence item: 6009

python main.py --method fptree --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.1 --min_conf 0.6
method: fptree
32.23 sec
find 1495 item set
confidence item: 1604

python main.py --method fptree --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.3 --min_conf 0.1
method: fptree
1.05 sec
find 50 item set
confidence item: 9

python main.py --method fptree --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.3 --min_conf 0.6
method: fptree
1.08 sec
find 50 item set
confidence item: 7

python main.py --method apriori --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.1 --min_conf 0.1
method: apriori
81.68 sec
find 1495 item set
confidence item: 6009

python main.py --method apriori --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.1 --min_conf 0.6
method: apriori
80.99 sec
find 1495 item set
confidence item: 1604

python main.py --method apriori --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.3 --min_conf 0.1
method: apriori
0.88 sec
find 50 item set
confidence item: 9

python main.py --method apriori --dataset ./inputs/2022-DM-release-testdata-2.data --min_sup 0.3 --min_conf 0.6
method: apriori
0.87 sec
find 50 item set
confidence item: 7

```