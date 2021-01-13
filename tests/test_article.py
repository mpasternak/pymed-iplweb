import os
import xml.etree.ElementTree as ET

import pytest
from pymed.article import PubMedArticle


@pytest.fixture
def test_xml1():
    return os.path.join(os.path.dirname(__file__), "testdata", "test1.xml")


@pytest.fixture
def test_xml1_data(test_xml1):
    return open(test_xml1).read()


@pytest.fixture
def test_xml1_element(test_xml1_data):
    return ET.fromstring(test_xml1_data)


@pytest.fixture
def test_article1(test_xml1_element):
    return PubMedArticle(test_xml1_element)


def test_pubmed_id(test_article1):
    assert test_article1.pubmed_id == 33374571


def test_pmc_id(test_article1):
    assert test_article1.pmc_id == "PMC7793075"


def test_doi(test_article1):
    assert test_article1.doi == "10.3390/ijms22010056"
